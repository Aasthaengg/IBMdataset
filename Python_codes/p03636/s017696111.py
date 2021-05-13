#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s=input()
k=len(s)-2
print("{0}{1}{2}".format(s[0],str(k),s[-1]))