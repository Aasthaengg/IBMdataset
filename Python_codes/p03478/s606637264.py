N, A, B = map(int, input().split())

def sum_of_digits(n):
   result   = 0
   quotient = n
   while quotient:
       result   +=  quotient % 10
       quotient //= 10
   return result

ans = 0
for i in range(1, N + 1):
    sd = sum_of_digits(i)
    if sd >= A and sd <= B:
        ans += i

print(ans, flush=True)
