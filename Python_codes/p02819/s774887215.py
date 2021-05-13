def prime_list(num):
    list = [0]*2 + [1]*(num - 1)
    prime_list = []
    for i in range(2,num + 1):
        if list[i] == 1:
            for j in range(2, num//i + 1):
                list[i*j] = 0
    for i in range(num + 1):
        if list[i] == 1:
            prime_list.append(i)
    return prime_list

x = int(input())
prime = prime_list(100003)

while x not in prime:
    x += 1

print(x)