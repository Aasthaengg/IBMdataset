N = int(input())
s = input()
t = input()

for i in range(N):
    tmp = 0
    while True:
        if s[i+tmp] == t[tmp]:
            pass
        else:
            break

        tmp += 1
        if not i + tmp < N:
            print(i + N)
            exit(0)
print(2*N)