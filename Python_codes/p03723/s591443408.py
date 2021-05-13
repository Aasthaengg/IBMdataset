# my solution
*a, = map(int,input().split())
if any(map(lambda x: bin(x)[-1]== "1", a)):
    print("0")
    exit()
a = [bin(abs(a[i+1]-a[i]))[::-1].find('1') for i in range(2)]
print(max(a) if a[0]*a[1]<0 else min(a))