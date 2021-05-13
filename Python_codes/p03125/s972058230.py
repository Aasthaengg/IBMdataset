a, b = map(int, input().split())
print((-1)**(b%a != 0)*a+b)