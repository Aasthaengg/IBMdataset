a, b, c = map(int, input().split())
a_sho,b_sho,c_sho = a,b,c
ans = 0
mugen = False
while True:
    a_k = a
    b_k = b
    c_k = c
    if a%2 != 0 or b%2 != 0 or c%2 != 0:
        break
    else:
        a = b_k/2 + c_k/2
        b = a_k/2 + c_k/2
        c = a_k/2 + b_k/2
        ans += 1
    if a == a_sho and b == b_sho and c == c_sho:
        mugen = True
        break

if mugen:
    print(-1)
else:
    print(ans)