import math
def main():
  s = input()
  min=abs(int(s[:3])-753)
  for i in range(1,len(s)-2):
    if abs(int(s[i:i+3])-753)<min:
      min=abs(int(s[i:i+3])-753)
  print(min)
main()