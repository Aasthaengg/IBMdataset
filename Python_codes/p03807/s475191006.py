n = int(input())
num_list = list(map(int, input().split()))
guki = len([i for i in num_list if i%2==1])
print('YES' if guki%2==0 else 'NO')