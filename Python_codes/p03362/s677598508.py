N = int(input())

def find_prime(n):
    prime_list = []
    find_list = list(range(2,n+1))
    while True:
        if find_list[0] > n**(1/2):
            prime_list.extend(find_list)
            break
        else:
            head = find_list[0]
            prime_list.append(head)
            find_list.pop(0)
            find_list = [num for num in find_list if num % head != 0]
    return prime_list

prime = find_prime(5555)
five = []
for num in prime:
    if num%5 == 1:
        five.append(num)

ans = []
for num in range(N):
    ans.append(five[num])

print(*ans)