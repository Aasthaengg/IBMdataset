input()
*p,=map(int,input().split())
print(sum(p[i]<p[i+1]<p[i+2] or p[i]>p[i+1]>p[i+2]for i in range(len(p)-2)))