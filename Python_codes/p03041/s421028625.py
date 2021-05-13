import sys 

num = list(map(int, input().split()))

input= sys.stdin.readline()
def convert(str,number):
  num = number-1
  str_one = str[num].lower()
  return str[0:num]+str_one+str[number:]
print(convert(input,num[1]))