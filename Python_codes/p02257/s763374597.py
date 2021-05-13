def prime_number(a):
    if a ==2 : return True

    if not a==1 and not a%2==0:
        k = 3
        while k <= a**(1/2):
            if a % k == 0:
                return False
                break
            k += 2
        return True


count_pn = 0
for i in range(int(input())):
    a = int(input())
    if prime_number(a):
        count_pn += 1
print(count_pn)