import sys

N=int(input())
lo,hi = 0,N-1
print(lo,"\n")
sys.stdout.flush()
val_lo = input()
if val_lo == 'Vacant':exit()
print(hi,"\n")
sys.stdout.flush()
val_hi = input()
if val_hi == 'Vacant':exit()

while True:
  m = (lo+hi)//2
  print(m,"\n")
  sys.stdout.flush()
  val_m = input()
  if val_m == 'Vacant':exit()
  if ((m-lo) % 2 == 0 and val_lo != val_m) or ((m-lo) % 2 and val_lo == val_m):
    hi = m
    val_hi = val_m
  else:
    lo = m
    val_lo = val_m