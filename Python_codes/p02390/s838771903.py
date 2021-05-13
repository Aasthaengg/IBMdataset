num_time = int(raw_input())
x = []
num_z = num_time/3600
num_h = (num_time%3600)/60
num_b = (num_time%3600)%60
x.append(num_z)
x.append(num_h)
x.append(num_b)
x = map(str, x)
print ":".join(x)