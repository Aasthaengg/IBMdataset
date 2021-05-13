n = int(input())
L = list(map(int,input().split()))

li = [abs(L[i]-sum(L)/len(L)) for i in range(n)]

print(li.index(min(li)))