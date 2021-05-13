N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

na, nb = 0, 0

suma = sum(a)
sumb = sum(b)
jdg = False

for i in range(N):
    while a[i]!= b[i]:
        if suma + na > sumb + nb:
            jdg = True
            break
        if i == N - 1:
            a[i] += na
            b[i] += nb
            if a[i] > b[i]:
                jdg = True
            break
        if a[i] > b[i]:
            ab = a[i] - b[i]
            if nb < ab:
                na += 2 * (ab - nb)
                nb = 0
            else: nb -= ab
            sumb += ab
            b[i] += ab
        else:
            ba = b[i] - a[i]
            if na < ba:
                nb += (ba - na + 1) // 2
                na = 0
            else: na -= ((ba+1)//2)*2
            if nb > 0: nb -= ba%2
            else: na += 2 * (ba%2)
            suma += ((ba+1)//2)*2
            sumb += ba%2
            a[i] += ((ba+1)//2)*2
            b[i] += ba%2
    if jdg: break
print('No' if jdg else 'Yes')