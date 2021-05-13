def order(x):
    return (x + 9) // 10 * 10

def wait(x):
    return order(x) - x

dishes = [int(input()) for _ in range(5)]
total = sum(order(i) for i in dishes)
total -= max(wait(i) for i in dishes)
print(total)
