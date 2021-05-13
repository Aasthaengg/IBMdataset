sample = input()
#new = list(sample)
#if "A" in new:
a_pos = sample.index('A')
#if "Z" in new:
z_pos = sample.rfind('Z')
print(z_pos-a_pos+1)


