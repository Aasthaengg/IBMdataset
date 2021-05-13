a, b= map(int, input().split())

input_list = []
input_list.append(a+b)
input_list.append(a-b)
input_list.append(a*b)

input_list.sort(reverse=True)

print(input_list[0])