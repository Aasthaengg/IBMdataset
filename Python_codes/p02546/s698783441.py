input_date = input()
input_length = len(input_date)
input_end = input_date[input_length - 1]

if (input_end == "s"):
  print(input_date + "es")
else:
  print(input_date + "s")