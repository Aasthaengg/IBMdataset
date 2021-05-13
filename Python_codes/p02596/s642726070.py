K = int(input())
a = []
a.append(7%K)
for i in range(1, K+1):
    a.append((a[-1]*10 + 7) % K)
for i in range(K+1):
    if a[i] == 0:
        print(i+1)
        break
else:
    print(-1)