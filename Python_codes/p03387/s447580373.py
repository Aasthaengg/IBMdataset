a,b,c = map(int, input().split())

s = a+b+c
cnt = 0
while not (s%3==0 and s//3 >= a and s//3 >= b and s//3>= c):
    s += 2
    cnt += 1
print(cnt)