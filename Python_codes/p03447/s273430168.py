x = int(input())
a = int(input())
b = int(input())
after_cake = x - a
after_daughnut = after_cake - b*(after_cake//b)
print(after_daughnut)