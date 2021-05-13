k,a,b = map(int, input().split( ))
if a>=b-2 or k<=a:##
    print(k+1)
    exit()

cnt = a 
k -= a-1


ch = k//2 

cnt += (b-a)*ch 
cnt += k%2
print(cnt)