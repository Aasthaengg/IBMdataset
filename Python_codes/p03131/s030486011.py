k,a,b = map(int, input().split())
print(k+1 if b-a <= 2 else a + ((k-a+1)//2*(b-a) + ((k-a+1)%2)))