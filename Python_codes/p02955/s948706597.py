n, k =  map(int,input().split())
a_list = list(map(int,input().split()))
total = sum(a_list)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

div_list = make_divisors(total)
for div in div_list:
    b_list = [a%div for a in a_list]
    b_list.sort()
    change = sum(b_list[:(-sum(b_list)//div)])
    if change <=k:
        print(div)
        break