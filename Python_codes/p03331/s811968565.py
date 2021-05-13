n = input()
print(10 if len(set(n)) == 2 and n[:2] == "10" else sum(int(i) for i in n))