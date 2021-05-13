answer_list = [1, 1] + [None] * 43

def fib(num):
    ans = answer_list[num]
    if ans:
        return ans
    ans = fib(num - 1) + fib(num - 2)
    answer_list[num] = ans
    return ans


n = int(input())

print(fib(n))