N = int(input())

def ask(n):
    print(n, flush=True)
    response = input().rstrip()[0]
    if response == 'V':
        exit()
    return response

def condition(start, middle, r_start, r_middle):
    if (middle-start)&1:
        return r_start == r_middle
    else:
        return r_start != r_middle

start = 0
end = N
r_start = ask(0)

for _ in range(19):
    middle = (start + end) // 2
    r_middle = ask(middle)
    if condition(start, middle, r_start, r_middle):
        end = middle
    else:
        start = middle
        r_start = r_middle

