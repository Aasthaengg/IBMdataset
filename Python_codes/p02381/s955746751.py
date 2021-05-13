import math

while True:
  total_scores = int(input())

  if total_scores == 0:
    break
  
  scores = [int(x) for x in input().split()]

  average_of_scores = sum(scores) / total_scores

  deviation_total = 0

  for score in scores:
    deviation_total += math.pow((score - average_of_scores), 2)

  variance = deviation_total / total_scores

  standard_deviation = math.sqrt(variance)  
  standard_deviation = "{:.8f}".format(standard_deviation)

  print(standard_deviation)

