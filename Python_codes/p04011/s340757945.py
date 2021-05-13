total_nights = int(input())
first_nights = int(input())
first_rate = int(input())
extra_rate = int(input())

if total_nights <= first_nights:
  total = total_nights * first_rate
else:
  total = (first_nights * first_rate) + ((total_nights - first_nights) * extra_rate)
print(total)
