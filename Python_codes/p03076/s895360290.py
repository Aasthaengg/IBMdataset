a = list(int(input()) for _ in range(5))
print(sum(map(lambda x:(x+9)//10*10, a))-max(map(lambda x:(10-x%10)%10, a)))