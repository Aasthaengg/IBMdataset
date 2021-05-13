def main():
    e = raw_input().split()
    t = list()

    for i in e:
        if i == '+': t.append(t.pop() + t.pop())
        elif i == '-': t.append(-(t.pop()) + t.pop())
        elif i == '*': t.append(t.pop() * t.pop())
        else: t.append(int(i))

    print(t.pop())
main()