N = int(input())

A = (N//100)*100
N -= A
B = (N//10)*10
N -= B

if 3 == N:
  print("bon")
elif 0==N or 1==N or 6==N or 8==N:
  print("pon")
else:
  print("hon")