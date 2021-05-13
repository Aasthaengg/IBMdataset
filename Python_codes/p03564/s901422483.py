n,k=[int(input()) for _ in range(2)]
num=1
for i in range(n):
    num_a=2*num
    num_b=num+k
    if num_a<num_b:
        num=num_a
    else:
        num=num_b
print(num)