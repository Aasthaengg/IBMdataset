def method_name(n, a, b):    
    plan1 = a * n
    plan2 = b
    return plan1, plan2

def main():
    n, a, b = map(int, input().split())
    plan1, plan2 = method_name(n, a, b)
    print(min(plan1, plan2))


main()