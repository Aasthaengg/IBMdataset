n = int(input())
la = list(map(int,input().split()))
lb = list(map(int,input().split()))
lc = list(map(int,input().split()))

con = 0

for i in range(n-1):
    if la[i+1]==la[i]+1:
        con += lc[la[i]-1]

print(sum(lb)+con)