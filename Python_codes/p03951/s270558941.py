N = int(input())
s = input()
t = input()

if s == t:
    print(N)
else:
    for i in range(N):
        if s[i:] == t[:N - i]:
            print(N + i)
            break
    else:
        print(2 * N)
