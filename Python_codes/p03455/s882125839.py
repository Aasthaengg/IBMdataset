a,b = map(int,input().split())

def answer(a: int ,b: int) ->int:
    if a * b % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(answer(a,b))