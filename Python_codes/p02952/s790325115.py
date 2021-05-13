N  = int(input())
def divisor(n):
    div_list = []
    for i in range(1, int(1+ n**0.5)):
        if n%i == 0 and i**2 == n:
            div_list.append(i)
        elif n%i == 0:
            div_list.append(i)
            div_list.append(int(n/i))
    return div_list
counter = 0

for i in range(1,N+1):
    if len(str(i)) % 2 == 1:
        counter += 1
        
print(counter)