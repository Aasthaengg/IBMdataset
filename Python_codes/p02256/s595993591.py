def sort_two_nums_tuple(x,y):
    return max(x,y),min(x,y)

def calculate_gcd(x,y):
    remain = float('inf')
    while remain != 0:
        remain = x % y
        x = y
        y = remain
    return x

input_x,input_y = map(int,input().split())
x,y = sort_two_nums_tuple(input_x,input_y)
ans = calculate_gcd(x,y)
print(ans)
