n = int(input())
p = list(map(int, input().split()))
print(sum(p[i-2]<p[i-1]<=p[i] or p[i]<p[i-1]<=p[i-2] or \
            p[i]==p[i-2]<p[i-1] for i in range(2,n)))