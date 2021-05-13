n_sheep ,n_wolves = input().split()
n_sheep , n_wolves = int(n_sheep),int(n_wolves)

if n_sheep > n_wolves:
  print('safe')
else:
  print('unsafe')
