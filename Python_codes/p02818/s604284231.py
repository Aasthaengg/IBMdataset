a_m, b, k = map(int, input().split())
a = max(0,a_m-k)
b = max(0,b-(k-(a_m-a)))
print(str(a)+" "+str(b))