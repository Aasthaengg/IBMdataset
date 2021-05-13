n = int(input())
a_list = list(map(int,input().split()))

def count(sign):
    
    count = 0
    a_sum = 0
    for a in a_list:
        a_sum +=a
        if a_sum*sign <= 0: 
            ope = sign - a_sum
            a_sum += ope
            count += abs(ope)
        sign *= -1
    return count
print(min(count(1),count(-1)))
