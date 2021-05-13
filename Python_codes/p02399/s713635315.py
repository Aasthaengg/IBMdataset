numbers = input().split()
numbers = list(map(int, numbers))

d=numbers[0]//numbers[1]
r=numbers[0]%numbers[1]
f=numbers[0]/numbers[1]

print(d,r,"{:.8f}".format(f))