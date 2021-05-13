N, A, B = map(int, input().split())

def int_to_sum(i):
    i_str = str(i)
    result = 0
    for i_s in i_str:
        result += int(i_s)
    return result

result = 0

for i in range(1,N+1):
    int_sum = int_to_sum(i)
    if int_sum <= B and int_sum >= A:
        result += i

print(result)
