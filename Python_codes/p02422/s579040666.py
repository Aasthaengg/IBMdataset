input_str = input()
n_orders = int(input())
for _ in range(n_orders):
    order_str = input()
    if order_str.startswith('print'):
        _, start, end = [s.strip() for s in order_str.split()]
        start = int(start)
        end = int(end) + 1
        print(input_str[start:end])
    elif order_str.startswith('reverse'):
        _, start, end = [s.strip() for s in order_str.split()]
        start = int(start)
        end = int(end) + 1
        rev_str = input_str[start:end]
        rev_str = list(reversed(rev_str))
        input_str = list(input_str)
        input_str[start:end] = rev_str
        input_str = ''.join(input_str)
    elif order_str.startswith('replace'):
        _, start, end, rep_str = [s.strip() for s in order_str.split()]
        start = int(start)
        end = int(end) + 1
        input_str = list(input_str)
        input_str[start:end] = rep_str
        input_str = ''.join(input_str)


