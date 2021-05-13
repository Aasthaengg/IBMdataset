in_str = input()
X = int(in_str)
in_str_a = input()
A = int(in_str_a)
in_str_b = input()
B = int(in_str_b)

answer = (X-A) - int((X-A)/B)*B
print(answer)