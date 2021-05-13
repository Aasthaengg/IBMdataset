a, b = map(int, input().split()) 
c = input()
d = c[:b-1] + c[b-1].lower() + c[b:]
print(str(d))