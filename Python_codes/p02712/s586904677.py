# FizzBuzzの整数部分の総和を求めよ

# FizzBuzz試し
# N = input()
# for i in range(1,int(N)+1):
#     if (i % 3 == 0) and (i % 5 == 0):
#         answer = 'FizzBuzz'
#     elif i % 3 == 0:
#         answer = 'Fizz'
#     elif i % 5 == 0:
#         answer = 'Buzz'
#     else:
#         answer = int(i)
#     print(answer)

N = input()
I = []
for i in range(1,int(N)+1):
    if (i % 3 != 0) and (i % 5 != 0):
        I.append(i)
# print(I)
Sum = sum(I)
print(Sum)