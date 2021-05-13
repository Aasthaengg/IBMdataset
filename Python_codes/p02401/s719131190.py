class SimpleCalculator:
    def calc(self, a, op, b):
        if op == '+':
            print a + b
        elif op == '-':
            print a - b
        elif op == '*':
            print a * b
        elif op == '/':
            print a / b

if __name__ == "__main__":
    sc = SimpleCalculator()
    while True:
        a, op, b = map(str, raw_input().split())
        if op == "?":
            break
        sc.calc(int(a), op, int(b))