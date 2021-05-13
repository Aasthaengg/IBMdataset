n = int(input())
p = list(map(int,input().split()))
count = 0

if n <= 2:
    print(0)
else:

    for i in range(0,n-2):
        for h in range(i+1,n-1):
            for j in range(h+1,n):
                if (abs(p[i]-p[h]) < p[j] < p[i]+p[h]) and (p[i] != p[h] and p[h] != p[j] and p[j] != p[i]):

                    count += 1

    print(count)
